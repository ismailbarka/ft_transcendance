"use client"
import React from 'react'
import classes from './progressBarFr.module.css'

const calculateLevel = (rating: number): number => {
  return Math.floor(rating / 100) + 1;
}

const calculatePercentage = (rating: number): number => {
  return rating % 100;
}

interface ProgressBarFrProps {
  ratingFr: number;
}

const ProgressBarFr: React.FC<ProgressBarFrProps> = ({ ratingFr }) => {
  const rating = ratingFr || 0; 
  const level = calculateLevel(rating);
  const percentage = calculatePercentage(rating);

  return (
    <div className={classes.container}>
      <div className={classes.Fr} style={{ width: `${percentage}%` }}></div>
      <div className={classes.textContainer}>
        <p className={classes.level}>Level {level} - {percentage}%</p>
      </div>
    </div>
  );
}

export default ProgressBarFr;
