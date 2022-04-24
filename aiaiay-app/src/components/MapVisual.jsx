import React from 'react';
import ReactDOM from "react-dom";
import { makeStyles } from '@material-ui/core/styles';
import ImageCard from './ImageCard';
import places from '../static/values';
import useWindowPosition from '../hook/useWindowPosition';

const useStyles = makeStyles({
  root: {
    maxWidth: 645,
    background: 'rgba(0,0,0,0.5)',
    margin: '20px',
  },
  media: {
    height: 440,
  },
  title: {
    fontFamily: 'Darker Grotesque',
    fontWeight: 'bold',
    fontSize: '2rem',
    color: '#fff',
  },
  desc: {
    fontFamily: 'Darker Grotesque',
    fontSize: '1.1rem',
    color: '#ddd',
  },
});

export default function ImageCard({ place, checked }) {
  const classes = useStyles();
    render() {
      return <iframe src="https://www.youtube.com/embed/cWDJoK8zw58" />;
    }

}
ReactDOM.render(<App />, document.getElementById("container"));