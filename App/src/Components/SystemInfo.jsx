import axios from "axios";
import "./Styles/SystemInfo.css";
import { useEffect, useState } from "react";

const URL = process.env.REACT_APP_URL;

const SystemInfo = () => {
    const get_cpu_info = async () => {
        const response = await axios.get(URL + "/system/cpu");
        setCpu(response.data);
    };
    const get_memory_info = async () => {
        const response = await axios.get(URL + "/system/memory");
        setMemory(response.data.virtual);
    };
    const [cpu, setCpu] = useState({
        usage: 0,
        freq: [0],
        times: [0, 0, 0, 0],
    });
    const [memory, setMemory] = useState({
        total: 0,
        used: 0,
        percent: 100,
    });
    useEffect(() => {
        const timer = setInterval(() => {
            get_cpu_info();
            get_memory_info();
        }, 1000);

        return () => clearInterval(timer);
    }, []);
    return (
        <div id="systemInfo">
            <div className="titleWrap">시스템 정보</div>
            <div className="contentWrap">
                <div className="listWrap">
                    <div className="item">
                        <div className="itemName">CPU</div>
                        <div className="itemInfo">
                            <div className="row">
                                <div className="key">사용률</div>
                                <div className="value">{cpu.usage}%</div>
                            </div>
                            <div className="row">
                                <div className="key">동작속도</div>
                                <div className="value">
                                    {cpu.freq[0] === undefined
                                        ? "-"
                                        : cpu.freq[0] / 1000 + "Ghz"}
                                </div>
                            </div>
                            <div className="row">
                                <div className="key">사용시간</div>
                                <div className="value">
                                    {cpu.times[3] === undefined
                                        ? "-"
                                        : `${(cpu.times[3] / 360000).toFixed(
                                              0
                                          )}시간 ${
                                              (cpu.times[3] / 6000).toFixed(0) %
                                              60
                                          }분`}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="item">
                        <div className="itemName">메모리</div>
                        <div className="itemInfo">
                            <div className="row">
                                <div className="key">사용률</div>
                                <div className="value">
                                    {(100 - memory.percent).toFixed(1)}%
                                </div>
                            </div>
                            <div className="row">
                                <div className="key">전체</div>
                                <div className="value">
                                    {(
                                        memory.total /
                                        1024 /
                                        1024 /
                                        1024
                                    ).toFixed(1)}
                                    GB
                                </div>
                            </div>
                            <div className="row">
                                <div className="key">사용중</div>
                                <div className="value">
                                    <div className="value">
                                        {(
                                            memory.used /
                                            1024 /
                                            1024 /
                                            1024
                                        ).toFixed(1)}
                                        GB
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SystemInfo;
