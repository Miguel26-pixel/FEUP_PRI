import * as React from "react";
import PropTypes from 'prop-types';

Card.propTypes = {
    MusicData: PropTypes.array,
}

export default function Card(props) {
    const musicData = props.MusicData;
    return (
        <div class="card" style={{height: "10%", width: "30%", marginTop: "2%",marginLeft: "35%",}}>
        <div class="card-header">
            Title: {musicData.title}
        </div>
        <div class="card-body">
            <h5 class="card-title">Artist: {musicData.artist}</h5>
            <p class="card-text">Album: {musicData.album}</p>
            <a href="#" class="btn btn-primary" style={{float: "inline-end"}}>See lyrics</a>
        </div>
        </div>
    )
}