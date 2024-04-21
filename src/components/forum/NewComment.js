import React, { useState } from 'react';
import { firestore as firestone } from '../../firebaseConfig';

const NewComment = ({ userId }) => {
  const [comment, setComment] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (comment.trim() === "") return;

    try {
      await firestone.collection('comments').add({
        content: comment,
        createdAt: new Date(),
        userId: userId, // 这里假设你已经有用户ID
      });
      setComment('');
    } catch (error) {
      console.error("Error adding comment: ", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        placeholder="写下你的评论..."
      />
      <button type="submit">发表评论</button>
    </form>
  );
};

export default NewComment;
