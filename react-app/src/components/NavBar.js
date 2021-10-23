
import React from 'react';
import { NavLink } from 'react-router-dom';
// import LogoutButton from './auth/LogoutButton';
// import { NavBar } from 'bootstrap'
import miniLogo from "../images/mywildestfantasylogoRough46.jpg"

const NavBar = () => {
  return (
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">
        <img src={miniLogo} class="d-inline-block align-top" alt="logo mwf"/>
        My Wildest Fantasy
      </a>
      {/* <span class="navbar gap">--</span> */}
      <div class="collapse navbar-collapse d-inline-block align-top" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <button class="btn bg-primary " type="button">
                League Home 
              </button>    
            </a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <button class="btn bg-primary " type="button">
                Message Board 
              </button>    
            </a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-aspopup="true" aria-expanded="false">
              <button class="btn bg-primary " type="button">
                My Team 
              </button>    
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a class="dropdown-item" href="#">View Roster</a>
              <a class="dropdown-item" href="#">Set Lineup</a>
              <a class="dropdown-item" href="#">Add/Drop</a>
              <a class="dropdown-item" href="#">Injured Reserve</a>
            </div>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <button class="btn bg-primary " type="button">
                
              </button>    
            </a>
          </li>
        </ul>
      </div>

    </nav>
  );
}

export default NavBar;
