import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const token = 'BQA65DgASbDjLn_Qkef11UyJVoRmfhIN4GyvqX1zleCMcbIWZVfJ-3txcUsJqSVi6zEuXWfugFpcMssy2IzYkl5XyZKJW5PbnkRHoXGgcmCW9aGtDRL0zxfzlIC6D75wRJvFhl6c6sXI4Q';
  const artistID = '3qZ2n5keOAat1SoF6bHwmb';
  const [artistName, setArtistName] = useState("");

  useEffect(() => {
    fetch('/get_artist/' + token + '/' + artistID).then(res => res.json()).then(data => {
      setArtistName(data.name);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>{artistName}</p>
      </header>
    </div>
  );
}

export default App;
