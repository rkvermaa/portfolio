import { useState } from 'react';
import './Hero.css';

const Hero = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        {/* Left Column - Image */}
        <div className="hero-image-container">
          <img 
            src="/profile pic website.png" 
            alt="Profile" 
            className="hero-image"
          />
          <div className="image-credit">
            © Photo credit
          </div>
        </div>
        {/* Right Column - Text */}
        <div className="hero-text">
          <h1 className="greeting">
            <span class="wave" aria-hidden="true">👋 </span>
            <span>Hi, I’m Ravi</span>
        </h1>
          <p className="intro-text">
            I'm currently working on{' '}
            <a href="#project" className="highlight-link">
              Your Project
            </a>
            , describe what you're building or working on.
          </p>
          
          <p className="additional-info">
            I also work on{' '}
            <a href="#work" className="highlight-link">
              other projects
            </a>
            {' '}and do{' '}
            <a href="#activities" className="highlight-link">
              interesting activities
            </a>
            . Add more details about your work and achievements here.
          </p>

          <a href="/about" className="learn-more">
            Learn more about me →
          </a>
        </div>
      </div>
    </div>
  );
};

export default Hero;