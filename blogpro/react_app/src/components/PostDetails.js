jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostDetails({ match }) {
  const [post, setPost] = useState({});

  useEffect(() => {
    axios.get(`/api/posts/${('http://127.0.0.1:8000/blogapp/post/')}`)
      .then(response => setPost(response.data))
      .catch(error => console.error(error));
  }, [('http://127.0.0.1:8000/blogapp/post/')]);

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  );
}

export default PostDetails;