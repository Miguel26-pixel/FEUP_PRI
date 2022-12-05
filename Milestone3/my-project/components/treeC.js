import Image from 'next/image';
import img from '../public/bg-image.png';
import {motion} from 'framer-motion';
import { treeWrapper } from '../variants.ts';

const TreeC = () => {
    return (
        <motion.div variants={treeWrapper} initial="initial" animate="animate" className="bottleWrapper">
            <Image src={img} style={{marginTop: "-1%", marginLeft: "-2%",}}/>
        </motion.div>
    );
};

export default TreeC;