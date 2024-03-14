import React from "react";
// import BannerBackground from "../Assets/home-banner-background.png";
import BannerImage from "../Assets/neon-guitar.png";
import Navbar from "./Navbar";
import { FiArrowRight } from "react-icons/fi";

const Home = () => {
  return (
    <div className="home-container">
      <Navbar />
      <div className="home-banner-container">
        <div className="home-bannerImage-container">
          {/* <img src={BannerBackground} alt="" /> */}
        </div>
        <div className="home-text-section">
          <h1 className="primary-heading" id="Home-id">
            Choose Your Favorite Guitar 
          </h1>
          <p className="primary-text">
          Top-quality electric guitar for sale, perfect for rocking out and making music!
          </p>
          <button className="secondary-button">
            Shop Now <FiArrowRight />{" "}
          </button>
        </div>
        <div className="home-image-section">
          <img src={BannerImage} alt="" />
        </div>
      </div>
    </div>
  );
};

export default Home;