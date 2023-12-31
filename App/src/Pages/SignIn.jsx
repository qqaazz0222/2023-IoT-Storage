import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Styles/Sign.css";
import IconBack from "../Images/IconLeft.png";

const URL = process.env.REACT_APP_URL;

const SignIn = () => {
    const navigate = useNavigate();
    const [id, setId] = useState("");
    const [pw, setPw] = useState("");
    const signIn = async () => {
        const response = await axios.post(URL + "/sign/in", { id: id, pw: pw });
        if (response.data !== null) {
            window.alert(`${response.data.id}님 반갑습니다.`);
            navigate("/summary");
        } else {
            window.alert("로그인 실패");
        }
    };
    return (
        <div id="signIn">
            <div className="header">
                <div
                    className="navWrap"
                    onClick={() => {
                        navigate("/");
                    }}
                >
                    <img src={IconBack} alt="" srcset="" />
                </div>
                <div className="titleWrap">로그인</div>
                <div className="funcWrap"></div>
            </div>
            <div className="body">
                <input
                    type="text"
                    name="id"
                    placeholder="아이디"
                    onChange={(e) => {
                        setId(e.target.value);
                    }}
                />
                <input
                    type="password"
                    name="pw"
                    placeholder="비밀번호"
                    onChange={(e) => {
                        setPw(e.target.value);
                    }}
                />
            </div>
            <div className="footer">
                <div className="btnWrap">
                    <button
                        onClick={() => {
                            signIn();
                        }}
                    >
                        로그인
                    </button>
                </div>
                <button
                    className="linkBtn"
                    onClick={() => {
                        navigate("/sign/up");
                    }}
                >
                    비밀번호를 잊었다면?
                </button>
            </div>
        </div>
    );
};

export default SignIn;
