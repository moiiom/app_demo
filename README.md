http服务器demo

主要使用微信爬取数据作为聚合站点数据，数据存放在elasticsearch名称

项目文件说明：
    scripts/
        create_index.sh     创建elasticsearch所有shell脚本
        load_index_data.py  加载爬虫爬取的微信公众号文章数据文件到elasicsearch指定的索引
        weixin.json         elasticsearch名称weixin索引mapping

    app_server.py           服务启动脚本，端口8888


本地启动服务：
    python app_server.py &


浏览器查看：
    http://localhost:8888
