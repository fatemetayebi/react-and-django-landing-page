// import React, { useState } from 'react';
// import axios from 'axios';
// import React, { useState } from 'react';
// // import './App.css';


// function Contact() {
//   const [inputValue, setInputValue] = useState('');

//   const handleButtonClick = () => {
//     // پاک کردن مقدار input
//     setInputValue('');

//     // پنهان کردن دکمه قبلی
//     document.getElementById('previousButton').style.display = 'none';

//     // نمایش input جدید با انیمیشن
//     document.getElementById('newInput').style.display = 'block';
//     document.getElementById('newButton').style.display = 'block';
//   };


//   const [email, setEmail] = useState('');
//   const [subject, setSubject] = useState('');
//   const [message, setMessage] = useState('');

//   const handleSubmit = (e) => {
//     e.preventDefault();

//     const sendEmailData = {
//       email: email,
//       subject: subject,
//       message: message
//     };

//     axios.post('http://127.0.0.1:8000/save_contact_form/send_email/', sendEmailData)
//       .then(response => {
//         console.log(response.data);
//         // Handle the response as needed
//       })
//       .catch(error => {
//         console.error(error);
//       });
//   };

//   return (

//     <div className="contact-page-wrapper" id="Contact-id" onSubmit={handleSubmit}>
//       <h1 className="primary-heading">Get In Touch With Us</h1>
      
//       <form onSubmit={handleSubmit}>
        // <input className="contact-form-container-email" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        // <input className="contact-form-container-subject" type="text" placeholder="Subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
        // <textarea className="contact-form-container-message" placeholder="Message" value={message} onChange={(e) => setMessage(e.target.value)} required />
        // <button className="secondary-button" type="submit">Send Email</button>
//       </form>
       

//       </div>
//   );
  
// }

// function Contact() {
//   const [inputValue, setInputValue] = useState('');

//   const handleButtonClick = () => {
//     // پاک کردن مقدار input
//     setInputValue('');

//     // پنهان کردن دکمه قبلی
//     document.getElementById('previousButton').style.display = 'none';

//     // نمایش input جدید با انیمیشن
//     document.getElementById('newInput').style.display = 'block';
//     document.getElementById('newButton').style.display = 'block';
//   };

//   return (
//     <div className="App">
//       <input type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
//       <button id="previousButton" onClick={handleButtonClick}>پاک کردن</button>
      
//       {/* Input و دکمه جدید */}
//       <div id="newInput" className="newInput" style={{ display: 'none' }}>
//         <input type="text" />
//         <button id="newButton">دکمه جدید</button>
//       </div>
//     </div>
//   );
// }


import { motion } from 'framer-motion';
import { useState } from 'react';
import axios from 'axios';


function Contact() {
  const [showNewInput, setShowNewInput] = useState(false);

  const [email, setEmail] = useState('');
  const [subject, setSubject] = useState('');
  const [message, setMessage] = useState('');

  const [entered_code, setCode] = useState('');

  const handleSubmitEmail = (e) => {
    e.preventDefault();
    setShowNewInput(true);

    const sendEmailData = {
      email: email,
      subject: subject,
      message: message
    };

    axios.post('http://127.0.0.1:8000/save_contact_form/send_email/', sendEmailData)
      .then(response => {
        console.log(response.data);
        // Handle the response as needed
      })
      .catch(error => {
        console.error(error);
      });
  };


  const handleSubmitCode = (e) => {
    e.preventDefault();
    setShowNewInput(true);

    const sendCode = {
      entered_code: entered_code
    };

    axios.post('http://127.0.0.1:8000/save_contact_form/get_code/', sendCode)
      .then(response => {
        console.log(response.data);
        // Handle the response as needed
      })
      .catch(error => {
        console.error(error);
      });
  };


  
  return (
    <div className="contact-page-wrapper" id="Contact-id">
      <h1 className="primary-heading">Get In Touch With Us</h1>
      
      <motion.form onSubmit={handleSubmitEmail} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
        {!showNewInput ? (
          <motion.div initial={{ x: -100, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
            <input className="contact-form-container-email" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input className="contact-form-container-subject" type="text" placeholder="Subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
            <textarea className="contact-form-container-message" placeholder="Message" value={message} onChange={(e) => setMessage(e.target.value)} required />
            <motion.button className="secondary-button" type="submit">Send Email</motion.button>
          </motion.div>
        ) : (
          <motion.div onSubmit={handleSubmitCode} initial={{ x: 100, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
            <input className="contact-form-container-subject" type="text" placeholder="enter code we sent to your email" value={entered_code} onChange={(e) => setCode(e.target.value)} required />
            <motion.button className="secondary-button" type="submit">submit</motion.button>
          </motion.div>
        )}
      </motion.form>
    </div>
  );
}
export default Contact;

