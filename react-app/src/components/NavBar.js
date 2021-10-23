
import React from 'react';
import { NavLink } from 'react-router-dom';
// import LogoutButton from './auth/LogoutButton';
import Button from 'react-bootstrap/Button'
import miniLogo from "../images/mywildestfantasylogoRough46.jpg"

const NavBar = () => {
  return (
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand font-weight-bolder" href="#">
        <img src={miniLogo} class="d-inline-block align-top" alt="logo mwf"/>
        My Wildest Fantasy
      </a>
      {/* <span class="navbar gap">--</span> */}
      <div class="collapse navbar-collapse d-inline-block align-top navbar-button-group" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <Button class="btn bg-primary font-weight-bolder btn-lg " type="button">
                League Home 
              </Button>    
            </a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <Button class="btn bg-primary font-weight-bolder btn-lg " type="button">
                Message Board 
              </Button>    
            </a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-aspopup="true" aria-expanded="false">
              <Button class="btn bg-primary font-weight-bolder btn-lg " type="button">
                Manage Roster 
              </Button>    
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a class="dropdown-item" href="#">View Roster</a>
              <a class="dropdown-item" href="#">Set Lineup</a>
              <a class="dropdown-item" href="#">Add/Drop</a>
              <a class="dropdown-item" href="#">Injured Reserve</a>
              <a class="dropdown-item" href="#">Current Matchup</a>
            </div>
          </li>
          <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLinkTwo" role="button" data-toggle="dropdown" aria-aspopup="true" aria-expanded="false">
              <Button class="btn bg-primary font-weight-bolder btn-lg" type="button">
                League Actions
              </Button>    
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLinkTwo">
              <a class="dropdown-item" href="#">View All Rosters</a>
              <a class="dropdown-item" href="#">Trade Center</a>
              <a class="dropdown-item" href="#">Free Agents</a>
              <a class="dropdown-item" href="#">League Standings</a>
              <a class="dropdown-item" href="#">Weekly Results</a>
              <a class="dropdown-item" href="#">Playoff Preview</a>
            </div>
          </li>
        </ul>
      </div>

    </nav>
  );
}

export default NavBar;
