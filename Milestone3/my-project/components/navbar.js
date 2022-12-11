import {motion} from 'framer-motion';
import { fadeInDown } from '../variants.ts';
import { useRouter } from 'next/router';


const Header = () => {
    const router = useRouter();
    return  (
        <motion.nav variants={fadeInDown} className="header" initial="initial" animate="animate">
            <span className = "header-logo" onClick={() => router.push('/')}>SPOTYFIND</span>
        </motion.nav>
    )
}

export default Header;