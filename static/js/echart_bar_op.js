// alert(disease);
// alert(xList);
// alert(yList);
require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });

        // 使用
        require(
            [
                'echarts',
                'echarts/chart/bar' // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('main'));

                var option = {
                    tooltip: {
                        show: true
                    },
                    legend: {
                        data:['关键词数']
                    },
                    xAxis : [
                        {
                            type : 'category',
                            interval: 0,
                            data : xList
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            "name":"关键词数",
                            "type":"bar",
                            "data":yList
                        }
                    ]
                };

                // 为echarts对象加载数据
                myChart.setOption(option);
            }
        );

// require.config({
//     paths: {
//         echarts: 'http://echarts.baidu.com/build/dist'
//     }
// });
//
// // 使用
// require(
//     [
//         'echarts',
//         //按需加载 (例如:使用柱状图就加载bar模块)
//         'echarts/chart/line',             //折线（面积）图
//         'echarts/chart/bar',             //柱状（条形）图
//         //'echarts/chart/scatter',        //散点（气泡）图
//         //'echarts/chart/k',             //K线图
//         //'echarts/chart/pie',             //饼（圆环）图
//         //'echarts/chart/radar',         //雷达（面积）图
//         //'echarts/chart/chord',         //和弦图
//         //'echarts/chart/force',         //力导向布局图
//         //'echarts/chart/map',             //地图
//         //'echarts/chart/gauge',         //仪表盘
//         //'echarts/chart/funnel',         //漏斗图
//         //'echarts/chart/eventRiver',    //事件河流图
//         //'echarts/chart/venn',         //韦恩图
//         //'echarts/chart/treemap',        //矩形树图
//         //'echarts/chart/tree',         //树图
//
//         'echarts/chart/wordCloud',    //字符云
//
//         //'echarts/chart/mix',             //混搭
//         //'echarts/chart/component',    //组件
//         //'echarts/chart/other',         //其他
//         //'echarts/chart/theme',         //主题
//         //'echarts/chart/topic',         //专题
//     ],
//     function (ec) {
//         // 基于准备好的dom，初始化echarts图表
//         var myChart = ec.init(document.getElementById('main'));
//
//         function createRandomItemStyle() {
//             return {
//                 normal: {
//                     color: 'rgb(' + [
//                         Math.round(Math.random() * 160),
//                         Math.round(Math.random() * 160),
//                         Math.round(Math.random() * 160)
//                     ].join(',') + ')'
//                 }
//             };
//         }
//
//         option = {
//             title: {
//                 text: ''
//
//             },
//             tooltip: {
//                 show: false
//             },
//             series: [{
//                 name: 'Google Trends',
//                 grid: {show:'true',borderWidth:'0'},
//                 type: 'Bar',
//                 // type: 'wordCloud',
//                 size: ['100%', '100%'],
//                 textRotation : [0, 45, 90, -45],
//                 textPadding: 0,
//                 autoSize: {
//                     enable: true,
//                     minSize: 14
//                 },
//                 data: [
//                     {
//                         name: "流感",
//                         value: 10000,
//                         itemStyle: {
//                             normal: {
//                                 color: 'black'
//                             }
//                         }
//                     },
//                     {
//                         name: "感冒",
//                         value: 6181,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "咳嗽",
//                         value: 4386,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "发烧",
//                         value: 4055,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "不舒服",
//                         value: 2467,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "孩子",
//                         value: 2244,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "妈妈",
//                         value: 1898,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "潮湿",
//                         value: 1484,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "妈妈",
//                         value: 1112,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "宝宝",
//                         value: 965,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "疫苗",
//                         value: 847,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "病毒",
//                         value: 5820,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "高发期",
//                         value: 555,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "接种",
//                         value: 550,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "广东",
//                         value: 462,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "板蓝根",
//                         value: 366,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "请假",
//                         value: 360,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "吃药",
//                         value: 2820,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "持续很久",
//                         value: 273,
//                         itemStyle: createRandomItemStyle()
//                     },
//                     {
//                         name: "看医生",
//                         value: 2650,
//                         itemStyle: createRandomItemStyle()
//                     }
//                 ]
//             }]
//         };
//
//         // 为echarts对象加载数据
//         myChart.setOption(option);
//     }
// );