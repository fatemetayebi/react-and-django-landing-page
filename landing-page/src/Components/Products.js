<<<<<<< HEAD
<<<<<<< HEAD
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import WheelPicker from 'react-simple-wheel-picker';

const Product = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/')
      .then(response => {
        console.log(response.data);
        setProducts(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);
=======
=======
>>>>>>> parent of e4a964a (140212141138)
import React from "react";
import PickMeals from "../Assets/pick-meals-image.png";
import ChooseMeals from "../Assets/choose-image.png";
import DeliveryMeals from "../Assets/delivery-image.png";
<<<<<<< HEAD
>>>>>>> parent of e4a964a (140212141138)
=======
>>>>>>> parent of e4a964a (140212141138)

const Work = () => {
  const workInfoData = [
    {
      image: PickMeals,
      title: "Pick Meals",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et sagittis duis elementum interdum facilisi bibendum.",
    },
    {
      image: ChooseMeals,
      title: "Choose How Often",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et ",
    },
    {
      image: DeliveryMeals,
      title: "Fast Deliveries",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et lorem ipsum",
    },
  ];
  return (
    <div className="work-section-wrapper">
      <div className="work-section-top">
        <p className="primary-subheading" id="Product-id"></p>
        <h1 className="primary-heading">Products</h1>
        <p className="primary-text">
        These electric guitar is a fantastic choice for any guitarist looking to elevate their playing experience.
        Don't miss out on this opportunity to own a top-notch instrument!
        </p>
      </div>
<<<<<<< HEAD
      <div className='work-section-products'>
        <WheelPicker style={{ width: 200, height: 150 }}>
          {products.map((data) => (
            <div className="work-section-info" key={data.intro}>
              <div className="product-boxes-img-container">
                <img src={data.image} alt="" />
              </div>
              <p>{data.title}</p>
              <p>{data.price}$</p>
            </div>
          ))}
        </WheelPicker>
=======
      <div className="work-section-bottom">
        {workInfoData.map((data) => (
          <div className="work-section-info" key={data.title}>
            <div className="info-boxes-img-container">
              <img src={data.image} alt="" />
            </div>
            <h2>{data.title}</h2>
            <p>{data.text}</p>
          </div>
        ))}
>>>>>>> parent of e4a964a (140212141138)
      </div>
    </div>
  );
};

export default Work;