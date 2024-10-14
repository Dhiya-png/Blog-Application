jsx
import React, { useState } from 'react';
import axios from 'axios';

function PostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/posts', { title, content })
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Title:</label>
      <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
      <br/>
      <label>Content:</label>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <br />
      <button type="submit">Create Post</button>
    </form>
  );
}

export default PostForm;
