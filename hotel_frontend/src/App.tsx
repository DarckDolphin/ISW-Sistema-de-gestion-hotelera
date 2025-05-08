import { ReactNode } from "react";
import React from "react";

interface Props {
  children: ReactNode
}

function App({children}: Props) {
  return (
    <>
      {children}
    </>
  );
}

export default App;
