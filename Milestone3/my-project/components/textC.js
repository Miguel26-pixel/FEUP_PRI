import {motion} from "framer-motion";
import { fadeInUp, staggerContainer } from "../variants.ts";
import { useRouter } from 'next/router';

const TextC = () => {
    const router = useRouter();
    return (
        <motion.div className="textContainer" variants={staggerContainer} initial="initial" animate="animate">

            <motion.div variants={fadeInUp} initial="initial" animate="animate"
            className="textContainer-middle">
                <span>SPOTYFIND</span>
            </motion.div>

            <div className="textContainer-bottom">
                <motion.button variants={fadeInUp} onClick={() => router.push('/search')}>Go to search</motion.button>
                <motion.p variants={fadeInUp}>
                    A new way to search the <span> musics </span> <br /> you really wanna hear!
                </motion.p>

            </div>
        </motion.div>
    )
}

export default TextC;