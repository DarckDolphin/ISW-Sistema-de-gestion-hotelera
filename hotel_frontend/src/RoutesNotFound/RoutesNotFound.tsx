import React from "react";
import { ReactNode } from "react";
import { Navigate, Route, Routes } from "react-router-dom";

interface Props {
  children: ReactNode;
}

export const RoutesNotFound = ({ children }: Props) => {
  return (
    <Routes>
      {children}
      <Route path="*" element={<Navigate to={"/404"} />} />
      <Route path="/404" element={<h2>Error. Page not found</h2>} />
    </Routes>
  );
};
