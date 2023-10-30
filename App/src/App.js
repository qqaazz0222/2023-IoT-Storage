// 라이브러리
import { BrowserRouter, Routes, Route } from "react-router-dom";
// 스타일
import "./App.css";
// 레이아웃

// 페이지
import Sign from "./Pages/Sign";
import SignIn from "./Pages/SignIn";
import Summary from "./Pages/Summary";
import Storage from "./Pages/Storage";
import SignUp from "./Pages/SignUp";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Sign />} />
                    <Route path="/sign/in" element={<SignIn />} />
                    <Route path="/sign/up" element={<SignUp />} />
                    <Route path="/summary" element={<Summary />} />
                    <Route path="/storage" element={<Storage />} />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;
