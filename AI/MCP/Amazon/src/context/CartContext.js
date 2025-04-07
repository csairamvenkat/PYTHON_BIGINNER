import React, { createContext, useContext, useReducer, useEffect } from 'react';

// Create context
const CartContext = createContext();

// Initial state
const initialState = {
  cart: [],
  totalItems: 0,
  totalAmount: 0,
};

// Actions
const ADD_TO_CART = 'ADD_TO_CART';
const REMOVE_FROM_CART = 'REMOVE_FROM_CART';
const UPDATE_QUANTITY = 'UPDATE_QUANTITY';
const CLEAR_CART = 'CLEAR_CART';

// Reducer function
const cartReducer = (state, action) => {
  switch (action.type) {
    case ADD_TO_CART: {
      const { product } = action.payload;
      const existingItemIndex = state.cart.findIndex(item => item.id === product.id);
      
      if (existingItemIndex >= 0) {
        // Product exists in cart, update quantity
        const updatedCart = [...state.cart];
        updatedCart[existingItemIndex] = {
          ...updatedCart[existingItemIndex],
          quantity: updatedCart[existingItemIndex].quantity + 1
        };
        
        return {
          ...state,
          cart: updatedCart,
          totalItems: state.totalItems + 1,
          totalAmount: state.totalAmount + product.price
        };
      } else {
        // Product doesn't exist in cart, add new item
        const newItem = {
          ...product,
          quantity: 1
        };
        
        return {
          ...state,
          cart: [...state.cart, newItem],
          totalItems: state.totalItems + 1,
          totalAmount: state.totalAmount + product.price
        };
      }
    }
    
    case REMOVE_FROM_CART: {
      const { productId } = action.payload;
      const existingItem = state.cart.find(item => item.id === productId);
      
      if (!existingItem) {
        return state;
      }
      
      const updatedCart = state.cart.filter(item => item.id !== productId);
      
      return {
        ...state,
        cart: up