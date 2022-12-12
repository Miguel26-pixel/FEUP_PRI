import React, { useRef, useLayoutEffect } from 'react'
import { useState, useEffect } from 'react';
import img from '../public/bg-image.png';
import Image from 'next/image';
import Header from '../components/navbar';
import Card from '../components/Card';
import api from './api/api';


function SearchPage() {
    const [musics, setMusics] = useState([]);
    const [query, setQuery] = useState("*:*");

    async function getMusics(query) {
      const results = await api.get("/search", {
        params: {
          q: query,
        }}, {
          headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      }});
        setMusics(results.data.docs);
    };

    const handleChange = (e) => {
      const val = e.target.value;
      setQuery(val);
    }


    useEffect(() => {
        getMusics(query);
    }, [query])

    return (<>
        <Image src={img} style={{marginTop: "-1%", marginLeft: "-2%", opacity: "0.6",zIndex: "-10", position: "absolute", float: 'inline-start'}} />        
        <Header></Header>
          <div className='sticky' style={{zIndex: "100", width: "30%", marginTop: "5%",marginLeft: "35%",}} >
              <input type="search" className="form-control" placeholder="Search for your favourite" aria-label="Search" onChange={handleChange}/>
          </div>
          {musics && musics.map((item) => (
                  <Card MusicData={item} key={item.id} />
              ))}
    </>
    );
}

export default function Search() {
    return <SearchPage />;
}