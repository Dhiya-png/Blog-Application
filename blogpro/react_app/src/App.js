import logo from './logo.svg';
jsx
import './App.css';
import React from 'react';
import PostList from './PostList';
import PostForm from './PostForm';
import { render } from '@testing-library/react';



function App() {
  return (
    <div>
    <h1>Blog App</h1>
    <PostList />
    <PostForm />
  </div>

  );
}

export default App;
ReactDOM.render(<App />, document.getElementById('root'));
