// src/components/Navbar.jsx
import { useState } from 'react';
import './Navbar.css';
import logoSvg from '/ravi.svg';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className="logo">
        <span className="logo-symbol">
            <svg version="1.1" viewBox="0 0 1280 1300" width="35" height="35" xmlns="http://www.w3.org/2000/svg">
            <path transform="translate(393,242)" d="m0 0h181l387 1 4 2 3 6 1 18v96l-5 5-3 1h-59l-75-2 1 2 1 32v129l-1 50-2 33-4 27-6 22-8 19-13 22-9 11-17 17-16 11-25 13-19 7-16 4-32 4-18 1-7 1-1 3 2 5 1 3 4 2 11 11 8 7 12 13 12 14 9 10 9 11 13 16 9 11 12 14 11 13 9 11 11 13 9 11 13 15 9 11 11 14 13 16 11 14 8 10 11 14 10 13 4 7-2 5-6 7-15 10-17 11-16 10-43 29-17 10-6 1-7-4-12-14-10-13-11-14-14-17-13-17-12-15-11-14-14-17-12-15-13-17-14-18-12-16-14-17-10-13-11-14-10-13-13-16-8-10-11-13-8-10-14-17-13-17-11-14-14-17-10-13-12-15-13-17-12-15-12-16-10-13-8-14 4-7 8-7 19-13 12-10 11-9 14-12 10-8 16-13 13-11 5-3 5 1 5 5 8 9 10 13 9 10 7 7 15 11 14 8 21 7 10 2h20l16-3 16-6 9-7 7-8 6-12 4-15 1-10 1-222-134 1h-195l-13-2-6-4-2-2v-45l1-64 2-6 5-5 3-1z" />
            <path transform="translate(966,370)" d="m0 0" />
            </svg>
        </span>
        <span className="logo-text">avi</span>
        <span className="logo-last-name-text">Verma</span>
      </div>
      
      <div className="nav-links">
        <a href="#home" className="nav-item">Home</a>
        <a href="#about" className="nav-item">About</a>
        <a href="#archive" className="nav-item">Archive</a>
        <a href="#life" className="nav-item">Life</a>
        
        <button 
          className={`more-menu-button ${isMenuOpen ? 'menu-open' : ''}`}
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          
        >
          <span className="button-text">
            {isMenuOpen ? '×' : '•••'}
          </span>
        </button>
        
        {isMenuOpen && (
          <div className="dropdown-menu">
            <a href="#projects">Projects</a>
            <a href="#blog">Blog</a>
            <a href="#contact">Contact</a>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;