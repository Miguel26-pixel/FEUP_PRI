import { useState, useEffect } from 'react';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Dialog from '@mui/material/Dialog';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import { useRouter } from 'next/router';
import Layout from '../components/Layout';
import Header from '../components/navbar';
import TextC from '../components/textC';
import TreeC from '../components/treeC';
import LeavesC from '../components/leavesC';
import {FormControl, InputLabel, Input, FormHelperText} from '@mui/material';

function MainPageContent() {
    const router = useRouter();
    const [openf, setOpenf] = useState(false);
    const [experiments, setExperiments] = useState(<></>)

    return (
        <>
        <div>
            <main>
                <TreeC />
                <TextC />
            </main>

            
        </div></>
    );
}

export default function MainPage() {
    return <MainPageContent />;
}