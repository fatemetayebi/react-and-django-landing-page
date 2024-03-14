import React, { useState } from 'react';
import axios from 'axios';



const Contact = () => {


  const [email, setEmail] = useState('');
  const [subject, setSubject] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

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

  return (

    <div className="contact-page-wrapper" id="Contact-id" onSubmit={handleSubmit}>
      <h1 className="primary-heading">Get In Touch With Us</h1>
      
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <input type="text" placeholder="Subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
        <textarea placeholder="Message" value={message} onChange={(e) => setMessage(e.target.value)} required />
        <button className="secondary-button" type="submit">Send Email</button>
      </form>

       



      </div>
  );
};

export default Contact;