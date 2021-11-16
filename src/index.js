import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";
import App from './App';
import  Header from './components/Header';
import Footer from './components/Footer';


const routing = (
  <Router>
      <Header />
      <Routes>
        <Route exact path = "/" element={<App />} />
      </Routes>
      <Footer />
  </Router>
);

ReactDOM.render(routing, document.getElementById('root'));