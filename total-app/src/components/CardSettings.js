import React from "react";
import { shortDescription,getMap } from "../utils/Utils";
import { motion } from 'framer-motion';

class CardSettings extends React.Component {
    render() {
        return (
            <motion.div
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="col-md-4 mb-4"
            >
                <div className="card" data-id={this.props.id}>
                    <img src={this.props.image} className="card-img-top" alt={this.props.name} />
                    <div className="card-body">
                        <h5 className="card-title">{this.props.name}</h5>
                        <p className="card-text">{shortDescription(this.props.description)}</p>
                        <p className="card-text">Цена: {this.props.price} руб</p>

                        <div className="container mt-2">
                            <div className="row justify-content-between">
                                <a href={"/about/" + this.props.id} className="btn btn-primary">Подробнее</a>
                                <a href="#" onClick={() => this.props.rmFrom(this.props.id)} className="btn btn-danger ml-2">{this.props.Text}</a>
                                { this.props.flagBasket &&
                                <>
                                <div className="btn-group">
                                    <button className="btn btn-outline-secondary" onClick={() => this.props.decreaseQuantity(this.props.id)}>-</button>
                                    <button className="btn btn-outline-secondary disabled">{getMap(JSON.parse(localStorage.getItem('basket'))).get(this.props.id)}</button>
                                    <button className="btn btn-outline-secondary" onClick={() => this.props.increaseQuantity(this.props.id)}>+</button>
                                </div>
                                </>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </motion.div>
        );
    }
}

export default CardSettings;