import Head from 'next/head';
import TextC from '../components/textC';
import TreeC from '../components/treeC';


export default function MainPage() {
    return (
    <><Head>
        <title>SPOTYFIND</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />

    </Head>

    <div>
        <main>
            <TreeC />
            <TextC />
        </main>

        
    </div>
    </>
);
    }