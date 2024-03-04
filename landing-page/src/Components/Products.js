import React, { useState, useEffect } from 'react';
import axios from 'axios';

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

  return (
    <div className="work-section-wrapper">
      <div className="work-section-top">
        <p className="primary-subheading" id="Product-id"></p>
        <h1 className="primary-heading">Products</h1>
        <p className="primary-text">
          Lorem ipsum dolor sit amet consectetur. Non tincidunt magna non et
          elit. Dolor turpis molestie dui magnis facilisis at fringilla quam.
        </p>
      </div>
      <div className="work-section-bottom">
        {products.map((data) => (
          <div className="work-section-info" key={data.intro}>
            <div className="info-boxes-img-container">
              <img src={data.image} alt="" />
            </div>
            <p>{data.title}</p>
            <p>{data.price}$</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Product;