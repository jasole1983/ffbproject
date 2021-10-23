
import React from 'react';
// import { NavLink } from 'react-router-dom';
// import LogoutButton from './auth/LogoutButton';
// import { NavBar } from 'bootstrap'
import miniLogo from "../images/mywildestfantasylogoRough46.jpg"

const NavBar = () => {
  return (
    <nav class="navbar nabar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">
        <img src={miniLogo} class="d-inline-block align-top" alt="logo mwf"/>
        My Wildest Fantasy
      </a>
      <span class="navbar gap">--</span>

    </nav>
  );
}

export default NavBar;
