import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Styles/Sign.css";
import IconBack from "../Images/IconLeft.png";

const URL = process.env.REACT_APP_URL;

const SignUp = () => {
    const navigate = useNavigate();
    const [id, setId] = useState("");
    const [pw, setPw] = useState("");
    const signUp = async () => {
        const response = await axios.post(URL + "/sign/up", { id: id, pw: pw });
        if (response.data !== null) {
            window.alert(`회원가입 성공( ID : ${response.data.id}).`);
            navigate("/sign/in");
        } else {
            window.alert("회원가입 실패");
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
                <div className="titleWrap">가입하기</div>
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
                            signUp();
                        }}
                    >
                        확인
                    </button>
                </div>
                <div className="infoWrap">
                    <a href="/">이용약관</a>
                    <a href="/">개인정보 정책</a>
                </div>
                <div className="agreeWrap">
                    <input type="checkbox" name="agree" id="agree" />
                    <label htmlFor="agree">동의합니다.</label>
                </div>
            </div>
        </div>
    );
};

export default SignUp;
