jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('/api/posts')
      .then(response => setPosts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <ul>
      {posts.map(post => (
        <li key={('http://127.0.0.1:8000/blogapp/post/?format=json')}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </li>
      ))}
    </ul>
  );
}

export default PostList;
