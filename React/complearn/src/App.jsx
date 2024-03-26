import { useState } from 'react';
import './App.css';


const SecNav = ()=>{
    return(
      <div>
        <img src="https://tse3.mm.bing.net/th?id=OIP.gRoFwE3C5t3CP6pzPlf_eQHaE8&pid=Api&P=0&h=180"></img>
      </div>
    )
  }

  const Info = (props)=>{
    return(
        <div>
            <h2></h2>
            <p>ipsum Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure ex amet nulla necessitatibus ipsum distinctio, eligendi quis aperiam consequatur, non ratione commodi magni. Maxime, rem est corrupti nesciunt veritatis ullam.</p>
        </div>
    )
  }

  function App() {
    return (
        <div>
          <h1 className="h1" >Hii I am <span>Mrunali</span></h1>
          <SecNav/>
          <Info name={'It is a nature'} Info={'it is '}></Info>
        </div>
    );
  }

  export default App;
  