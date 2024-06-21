import React from 'react';
import { motion } from 'framer-motion';

export const PageAnimation = ({ children }) => {
    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.7 }}
        >
            {children}
        </motion.div>
    );
};

