import React from 'react';
import '@testing-library/jest-dom/extend-expect'; // расширения для expect
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import App from './App';
import store from './core/store';

test('renders Application header', async () => {
  render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  const appHeader = await screen.findByText(/application/i);
  expect(appHeader).toBeInTheDocument();
});

test('renders Авторизация header', async () => {
  render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  const authHeader = await screen.findByText(/авторизация/i);
  expect(authHeader).toBeInTheDocument();
});

test('renders login button', () => {
  render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  const loginButton = screen.getByText(/войти/i);
  expect(loginButton).toBeInTheDocument();
});
