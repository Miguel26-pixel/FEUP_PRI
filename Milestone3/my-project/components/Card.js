import * as React from "react";
import PropTypes from 'prop-types';

Card.propTypes = {
    MusicData: PropTypes.object,
}

export default function Card(props) {
    const musicData = props.MusicData;
    return (
        <div className="card" style={{height: "10%", width: "30%", marginTop: "2%",marginLeft: "35%",}}>
        <div className="card-header">
            {musicData.title} 
        </div>
        <div className="card-body">
            <h5 className="card-title">Artist: {musicData.artist}</h5>
            <p className="card-text">Album: {musicData.album_name}</p>
            <a href="#" className="btn btn-primary" style={{float: "inline-end"}}>See lyrics</a>
        </div>
        </div>
    )
}