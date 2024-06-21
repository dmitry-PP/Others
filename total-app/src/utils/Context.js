import React,{createContext,useState} from "react";
import { getMap } from "./Utils";

export const AppStateContext = createContext();

// AppProvider.js


export const AppProvider = ({ children }) => {

    const savedFavourites = JSON.parse(localStorage.getItem('favourites')) || [];
    const [favouriteProducts, setFavouriteProducts] = useState(savedFavourites);

    const savedBasket = getMap(JSON.parse(localStorage.getItem('basket')));
    const [basket, setBasket] = useState(savedBasket);

    const appendToFavourites = (productId) => {
        console.log("from append")
        if( "favourites" in localStorage){
            let favourites = JSON.parse(localStorage.favourites);
            console.log(favourites.includes(productId),productId)
            if(favourites.includes(productId)) {
                favourites = favourites.filter((elem)=> elem!=productId)
                localStorage.setItem("favourites",JSON.stringify([...favourites]))
            }

            else localStorage.setItem("favourites",JSON.stringify([...favourites, productId]))
        }
        else{
            localStorage.setItem("favourites",JSON.stringify([ productId]))
        }

        setFavouriteProducts(JSON.parse(localStorage.getItem('favourites')) || [])
        
        //setTimeout(()=>console.log(localStorage.getItem("favourites"),'AppProvider Favourites'),0)
        
    };


    const appendToBasket = (productId) => {
        console.log("from append",localStorage.basket)
        if( "basket" in localStorage){
            let basket = getMap(JSON.parse(localStorage.basket));
            console.log(basket.has(productId),productId)
            if(basket.has(productId)) {
                basket.delete(productId)
            }
            else{
                basket.set(productId,1)
            }

            localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
        }
        else{
            let basket = new Map()
            basket.set(productId,1)
            localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
        }

        setBasket(getMap(JSON.parse(localStorage.getItem('basket'))) || new Map())
    };

    const increaseQuantity = (productId)=>{

        let basket = getMap(JSON.parse(localStorage.getItem('basket')))
        console.log(basket)

        basket.set(productId,+basket.get(productId)+1)
        localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
        setBasket(basket)

        console.log('increaseQuantity',+basket.get(productId))
    }

    const decreaseQuantity= (productId)=>{
        let basket = getMap(JSON.parse(localStorage.getItem('basket')))
        console.log(basket)
        let quantity = +basket.get(productId)
        if(quantity>1) basket.set(productId,quantity-1)
        else basket.delete(productId)
        localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
        setBasket(basket)
        console.log('decreaseQuantity',+basket.get(productId))


    }
    // const appendToBasket = (productId) => {
    //     console.log("from append",localStorage.basket)
    //     if( "basket" in localStorage){
    //         let basket = getMap(JSON.parse(localStorage.basket));
    //         console.log(basket.has(productId),productId)
    //         if(basket.has(productId)) {
    //             basket.set(productId,basket.get(productId)+1)
    //         }
    //         localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
    //     }
    //     else{
    //         let basket = new Map()
    //         basket.set(productId,1)
    //         localStorage.setItem("basket",JSON.stringify(Object.fromEntries(basket)))
    //     }

    //     setFavouriteProducts(getMap(JSON.parse(localStorage.getItem('basket'))) || new Map())
    // };


    return (
        <AppStateContext.Provider
            value={{
                appendToFavourites,
                appendToBasket,
                decreaseQuantity,
                increaseQuantity
            }}
        >
            {children}
        </AppStateContext.Provider>
    );
};

