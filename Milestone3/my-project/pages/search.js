import React, { useRef, useLayoutEffect } from 'react'
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import img from '../public/bg-image.png';
import Image from 'next/image';
import Header from '../components/navbar';
import Card from '../components/Card';
import data from "./MockData.json";

function SearchPage() {
    const router = useRouter();
    const [musics, setMusics] = useState(data);

    const getMusics = () => {};


    useEffect(() => {
        getMusics();
    }, [])

    const stickyHeader = useRef()
    useLayoutEffect(() => {
      const mainHeader = document.getElementById('search-div')
      let fixedTop = stickyHeader.current.offsetTop
      const fixedHeader = () => {
        if (window.pageYOffset > fixedTop) {
          mainHeader.classList.add('fixedTop') 
        } else {
          mainHeader.classList.remove('fixedTop')
        }
      }
      window.addEventListener('scroll', fixedHeader)
    }, [])


    return (<>
        <Image src={img} style={{marginTop: "-1%", marginLeft: "-2%", opacity: "0.6",zIndex: "-10", position: "absolute", float: 'inline-start'}} />        
        <Header></Header>
        <div className="form-outline" id="search-div" ref={stickyHeader} style={{zIndex: "100", width: "30%", marginTop: "5%",marginLeft: "35%",}} >
            <input type="search" id="form1" className="form-control" placeholder="Type query" aria-label="Search" />
        </div>
        {musics.map((item) => (
                <Card MusicData={item} key={item.title + item.artist} />
            ))}
    </>
    );
}

export default function Search() {
    return <SearchPage />;
}