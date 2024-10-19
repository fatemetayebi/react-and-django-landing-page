import React from 'react';
import AboutBackground from "../Assets/perpel-powder2.png";
// import AboutBackgroundImage from "../Assets/about-background-image.png";
// import { BsFillPlayCircleFill } from "react-icons/bs";


const About = () => {
    return (
      <div className="about-section-container">
        <div className="about-background-image-container">
          <img src={AboutBackground} alt="" />
        </div>
        <div className="about-section-image-container">
        </div>
        <div className="about-section-text-container" id="About-id">
          <p className="primary-subheading" ></p>
          <h1 className="primary-heading" >
          Exploring the World of Electric Guitars
          </h1>
          <p className="primary-text">
          Electric guitars are available in music stores, online retailers, and second-hand markets. They come in various styles, colors, and brands to suit different preferences and budgets. Known for their versatility and ability to produce a wide range of sounds, electric guitars are popular among beginners and experienced musicians alike.
          </p>
          <p className="primary-text">
            
          </p>
          
        </div>
      </div>
    );
  };
  

export default About