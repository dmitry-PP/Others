import React from "react";
import { motion } from 'framer-motion';


class Header extends React.Component{
    render(){
        return (
            <header>
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="#">Магазин продуктов</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr-auto">
                        <motion.li className={"nav-item " + this.props.Main}
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <a className="nav-link" href="/">Главная</a>
                            </motion.li>
                            <motion.li className={"nav-item " + this.props.Catalog}
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <a className="nav-link" href="/catalog">Каталог</a>
                            </motion.li>
                            <motion.li className={"nav-item " + this.props.Favourite}
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <a className="nav-link" href="/favourite">Избранное</a>
                            </motion.li>
                            <motion.li className={"nav-item " + this.props.Basket}
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <a className="nav-link" href="/basket">Корзина</a>
                            </motion.li>
                    
                            <motion.li className={"nav-item " + this.props.Order}
                                whileHover={{ scale: 1.1 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <a className="nav-link" href="/order">Заказ</a>
                            </motion.li>
                        </ul>
                    </div>
                </nav>
            </header>
        )
    }
}
export default Header;