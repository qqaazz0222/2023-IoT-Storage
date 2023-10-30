import { useNavigate } from "react-router-dom";
import "./Styles/Sign.css";
import IconBack from "../Images/IconLeft.png";

const SignUp = () => {
    const navigate = useNavigate();
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
                <input type="text" name="id" placeholder="아이디" />
                <input type="password" name="pw" placeholder="비밀번호" />
            </div>
            <div className="footer">
                <div className="btnWrap">
                    <button
                        onClick={() => {
                            navigate("/sign/in");
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
