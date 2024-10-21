import { motion } from 'framer-motion';
import React, { useState } from 'react';
import axios from 'axios';

axios.defaults.withCredentials = true;

function Contact() {
  
  const [showNewInput, setShowNewInput] = useState(false);

  const [email, setEmail] = useState('');
  const [subject, setSubject] = useState('');
  const [message, setMessage] = useState('');

  const [entered_code, setCode] = useState('');
  const [setData] = useState(null);
  const [setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmitEmail = (e) => {
    e.preventDefault();
    setShowNewInput(true);

    const sendEmailData = {
      email: email,
      subject: subject,
      message: message
    };

    console.log(sendEmailData.data);
    axios.post('http://127.0.0.1:8000/sendcode/', sendEmailData, {
      headers: {
        'Content-Type': 'application/json',
      } 
    })
    .then((response) => {
      setData(response.data); 
      if (response.data.session_key) {
        localStorage.setItem('session_key', response.data.session_key);
      }
      setLoading(false); 
    })
      .then((data) => {
        
      })  
      .catch(error => {
        console.error(error);
      });    
  };


  const handleSubmitCode = (e) => {
    e.preventDefault();
    setShowNewInput(true);

    const sessionKey = localStorage.getItem('session_key');

    const sendCode = {
      session_key: sessionKey,
      entered_code: entered_code
    };

    axios.post('http://127.0.0.1:8000/verify_code/', sendCode, {
      headers: {
        'Content-Type': 'application/json'
      },
    })

      .then(response => {
        console.log(response.data);
        setErrorMessage('YOUR MESSAGE SENT');
      })
      .catch(error => {

        console.error(error);

        if (error.response && error.response.status === 400) {
          setErrorMessage('Entered code is wrong');
        } else {
          setErrorMessage('An error occurred');
        }

      });
  
} 
//   if (sessionKey) {
//     console.log('sessionKey:', sessionKey);
//   } else {
//     console.error('sessionKey element not found.');
//   } 
//  };


  
  return (
   
    <div className="contact-page-wrapper" id="Contact-id">
      <h1 className="primary-heading">Get In Touch With Us</h1>

      {!errorMessage ? (
        !showNewInput ? (
          <motion.form onSubmit={handleSubmitEmail} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
            <motion.div initial={{ x: -100, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
              <input className="contact-form-container-email" name="email" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
              <input className="contact-form-container-subject" name="subject" type="text" placeholder="Subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
              <textarea className="contact-form-container-message" name="message" placeholder="Message" value={message} onChange={(e) => setMessage(e.target.value)} required />
              <motion.button className="secondary-button" type="submit">Send Email</motion.button>
            </motion.div>
          </motion.form>
        ) : (
          <motion.form onSubmit={handleSubmitCode} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
            <motion.div initial={{ x: 100, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
              <input className="contact-form-container-subject" type="text" placeholder="Enter code we sent to your email" value={entered_code} onChange={(e) => setCode(e.target.value)} required />
              <motion.button className="secondary-button" type="submit">Submit</motion.button>
            </motion.div>
          </motion.form>
          )
        ) : (
          <p style={{ color: 'white', marginTop: '20px' }}>{errorMessage}</p>
        )}
    </div>
  );
};

export default Contact;

