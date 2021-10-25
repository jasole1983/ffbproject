
import React from 'react';
import { NavLink } from 'react-router-dom';
// import Logoutbutton from './auth/Logoutbutton';
// import button from 'react-bootstrap/button'
import miniLogo from "../images/mywildestfantasylogoRough46.jpg"

const NavBar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <a className="navbar-brand font-weight-bolder" href="#">
        <img src={miniLogo} className="d-inline-block align-top" alt="logo mwf"/>
        My Wildest Fantasy
      </a>
      <div className="collapse navbar-collapse d-inline-block align-top navbar-button-group" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <NavLink exact to='/' className="nav-link">
              
                League Home 
                 
            </NavLink>
          </li>
          <li className="nav-item active">
            <NavLink to='/messageboard' exact={true} className="nav-link" >
              
                Message Board 
                  
            </NavLink>
          </li>
          <li className="nav-item dropdown">
            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              
                Manage Roster 
                 
            </a>
            <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a className="dropdown-item" href="#">View Roster</a>
              <a className="dropdown-item" href="#">Set Lineup</a>
              <a className="dropdown-item" href="#">Add/Drop</a>
              <a className="dropdown-item" href="#">Injured Reserve</a>
              <a className="dropdown-item" href="#">Current Matchup</a>
            </div>
          </li>
          <li className="nav-item dropdown">
          <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLinkTwo" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              
                League Actions
                
            </a>
            <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLinkTwo">
              <a className="dropdown-item" href="#">View All Rosters</a>
              <a className="dropdown-item" href="#">Trade Center</a>
              <a className="dropdown-item" href="#">Free Agents</a>
              <a className="dropdown-item" href="#">League Standings</a>
              <a className="dropdown-item" href="#">Weekly Results</a>
              <a className="dropdown-item" href="#">Playoff Preview</a>
            </div>
          </li>
        </ul>
      </div>

    </nav>
  );
}

export default NavBar;
