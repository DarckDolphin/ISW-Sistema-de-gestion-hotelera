import React from "react";
import { Navigate, Outlet } from "react-router-dom";

export  const AdminGuard = () => {
  const isAdmin = false;

  return isAdmin ? <Outlet/> : <Navigate to={"/private/dashboard"} replace/>
}
