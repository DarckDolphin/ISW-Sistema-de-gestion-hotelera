import React from "react";
import { BrowserRouter, Navigate, Route } from "react-router-dom";
import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import Reservas from "./pages/reservas";
import { RoutesNotFound } from "./RoutesNotFound/RoutesNotFound";
import { PrivateRouter } from "./auth/PrivateRouter";
import { AdminGuard } from "./auth/AdminGuard";
import { PrivateGuard } from "./auth/PivateGuard";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <RoutesNotFound>
        <Route path="/" element={<Navigate to={"/login"} />} />
        <Route path="/login" element={<Login />} />
        <Route element={<PrivateGuard />}>
          <Route path="/private/*" element={<PrivateRouter />} />
          <Route element={<AdminGuard />}>
            <Route path="/private/*" element={<PrivateRouter />} />
          </Route>
        </Route>
      </RoutesNotFound>
    </BrowserRouter>
  );
};
