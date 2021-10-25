
import React from 'react';
import { NavLink } from 'react-router-dom';
// import LogoutButton from './auth/LogoutButton';
import Button from 'react-bootstrap/Button'
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
            <a className="nav-link" href="#">
              <Button className="btn bg-primary font-weight-bolder btn-lg " type="button">
                League Home 
              </Button>    
            </a>
          </li>
          <li className="nav-item active">
            <NavLink to='/messageboard' exact={true} className="nav-link" >
              <Button className="btn bg-primary font-weight-bolder btn-lg " type="button">
                Message Board 
              </Button>    
            </NavLink>
          </li>
          <li className="nav-item dropdown">
            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <Button className="btn bg-primary font-weight-bolder btn-lg " type="button">
                Manage Roster 
              </Button>    
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
              <Button className="btn bg-primary font-weight-bolder btn-lg" type="button">
                League Actions
              </Button>    
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
