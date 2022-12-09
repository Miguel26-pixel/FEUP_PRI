import * as React from "react";
import Head from 'next/head';

export default function Layout({children}) {
    return (
        <><Head>
            <title>SPOTYFIND</title>
        </Head>
        <div>
            {children}
        </div>
        </>
    )
}


