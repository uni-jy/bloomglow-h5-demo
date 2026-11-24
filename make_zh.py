"""Generate zh.html from index.html by replacing interface copy. Run: python3 make_zh.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = (ROOT / "index.html").read_text(encoding="utf-8")

# Order matters only where one string contains another; longer strings first.
T = [
    # page shell
    ('<html lang="en" translate="no">', '<html lang="zh-CN" translate="no">'),
    ("<title>BLOOM GLOW · Creator H5 demo</title>", "<title>BLOOM GLOW · 达人端 H5 交互稿（中文）</title>"),
    ('<h1>BLOOM GLOW 达人端 H5 demo</h1>', '<h1>BLOOM GLOW 达人端 H5 demo（中文版）</h1>'),
    ('· 语言：<b>English</b> / <a href="zh.html">中文</a>', '· 语言：<a href="index.html">English</a> / <b>中文</b>'),
    ('const SELF = "index.html", OTHER = {file: "zh.html", label: "中文版"};',
     'const SELF = "zh.html", OTHER = {file: "index.html", label: "English"};'),
    ("<p>按达人从\"收到链接\"到\"日常查看\"的顺序排列，共 10 屏。",
     "<p>中文版仅供内部演示；面向美区达人的正式页面为英文。按达人从\"收到链接\"到\"日常查看\"的顺序排列，共 10 屏。"),

    # common
    ('<a class="link" href="#s9">Privacy</a>', '<a class="link" href="#s9">隐私</a>'),
    ("‹ Back", "‹ 返回"), ("‹ Schedule", "‹ 排期"),
    ("Step 1 of 2", "第 1 步 / 共 2 步"), ("Step 2 of 2", "第 2 步 / 共 2 步"),
    ('<span class="chip ok">Connected</span>', '<span class="chip ok">已连接</span>'),
    ('<span class="chip warn">Not connected</span>', '<span class="chip warn">未连接</span>'),
    ('<a class="on" href="#s5">Home</a>', '<a class="on" href="#s5">首页</a>'),
    ('<a href="#s5">Home</a>', '<a href="#s5">首页</a>'),
    ('<a class="on" href="#s6">Schedule</a>', '<a class="on" href="#s6">排期</a>'),
    ('<a href="#s6">Schedule</a>', '<a href="#s6">排期</a>'),
    ('<a class="on" href="#s8">Results</a>', '<a class="on" href="#s8">数据</a>'),
    ('<a href="#s8">Results</a>', '<a href="#s8">数据</a>'),
    ('<a class="on" href="#s9">Account</a>', '<a class="on" href="#s9">账号</a>'),
    ('<a href="#s9">Account</a>', '<a href="#s9">账号</a>'),

    # 1 landing
    ("For US TikTok Shop creators", "面向美区 TikTok Shop 达人"),
    ("Shoppable videos, made and posted for you.", "挂车视频，我们帮你做好、按时发出。"),
    ("We create product videos with our studio, attach a product from your showcase, and post them on a schedule you agreed to. Commissions go to your TikTok Shop account as usual.",
     "我们的工作室制作带货视频，挂上你橱窗里的商品，按约定的排期发布。佣金照常进你的 TikTok Shop 账户。"),
    ('<a class="btn" href="#s2">Connect TikTok Shop</a>', '<a class="btn" href="#s2">连接 TikTok Shop</a>'),
    ("<h3>How it works</h3>", "<h3>怎么合作</h3>"),
    ("<b>Connect once</b><span>Approve access on TikTok. About one minute.</span>",
     "<b>连接一次</b><span>在 TikTok 上同意授权，大约 1 分钟。</span>"),
    ("<b>We prepare each post</b><span>Video, product and caption are reviewed before scheduling.</span>",
     "<b>我们准备每一条视频</b><span>视频、商品和文案审核通过后才进入排期。</span>"),
    ("<b>Posts go live on schedule</b><span>Each video carries a product link and an AI-generated label.</span>",
     "<b>到点自动发布</b><span>每条视频都带商品链接和 AI 生成标识。</span>"),
    ("<b>See your results</b><span>Orders and commissions by video, updated daily.</span>",
     "<b>查看效果</b><span>按视频看订单和佣金，每天更新。</span>"),
    ("<h3>Clear boundaries</h3>", "<h3>边界写清楚</h3>"),
    ("<h4>We can</h4><ul><li>Post shoppable videos</li><li>Add products to your showcase</li><li>Read orders and video results</li></ul>",
     "<h4>我们可以</h4><ul><li>发布挂车视频</li><li>把商品加入你的橱窗</li><li>读取订单和视频数据</li></ul>"),
    ("<h4>We never</h4><ul><li>Move or withdraw money</li><li>See your password or DMs</li><li>See buyer addresses</li></ul>",
     "<h4>我们不会</h4><ul><li>转账或提现</li><li>看你的密码或私信</li><li>看买家地址</li></ul>"),
    ("BLOOM GLOW · operated with ReadyPost<br>Terms · Privacy · Contact", "BLOOM GLOW · 由 ReadyPost 提供技术支持<br>条款 · 隐私 · 联系我们"),

    # 2 check
    ("<h2 class=\"title\">Before you connect</h2>", "<h2 class=\"title\">连接前先确认</h2>"),
    ("TikTok checks these on your account. If one is missing, posting will fail later.",
     "TikTok 会检查你账号的这些条件；缺一项，后面发布会失败。"),
    ("US TikTok Shop creator<small>Showcase is on your profile</small>", "美区 TikTok Shop 达人<small>主页上有橱窗（Showcase）</small>"),
    ("1,000+ followers<small>Under 5,000: up to 3 shoppable videos a day</small>", "粉丝 1000 以上<small>不到 5000 粉时，每天最多 3 条挂车视频</small>"),
    ("<div>18+ and age verified</div>", "<div>已满 18 岁并完成年龄验证</div>"),
    ("<div>Identity verified and payout account added</div>", "<div>已完成实名验证并绑定收款账户</div>"),
    ("<div>Creator terms accepted</div>", "<div>已签署达人条款</div>"),
    ("<h3>What you'll approve on TikTok</h3>", "<h3>你将在 TikTok 上同意的权限</h3>"),
    ("<em>Profile</em><span>Your handle and sales region</span>", "<em>账号资料</em><span>你的用户名和销售地区</span>"),
    ("<em>Content posting</em><span>Upload and post shoppable videos, read video results</span>", "<em>内容发布</em><span>上传和发布挂车视频，读取视频数据</span>"),
    ("<em>Showcase</em><span>View and add products</span>", "<em>橱窗</em><span>查看和添加商品</span>"),
    ("<em>Affiliate orders</em><span>Orders and commissions from your content</span>", "<em>联盟订单</em><span>你内容带来的订单和佣金</span>"),
    ("I'm 18 or older, I've read the data notice, and I agree to the posting arrangement with BLOOM GLOW.",
     "我已满 18 岁，已阅读数据说明，并同意与 BLOOM GLOW 的代发布约定。"),
    ('<a class="btn plum" href="#s3">Continue to TikTok</a>', '<a class="btn plum" href="#s3">前往 TikTok 授权</a>'),
    ("Open this on the phone where you use TikTok.", "请在平时登录 TikTok 的手机上打开。"),

    # 3 tiktok mock
    ("<b>✕</b>Authorization", "<b>✕</b>授权"),
    ("Illustration based on TikTok's developer docs. The real page may differ.", "示意图，依据 TikTok 开发文档截图；真实页面为英文，以实际为准。"),
    ("<b>BLOOM GLOW</b> is requesting access to your account to get the following data via API",
     "<b>BLOOM GLOW</b> 正在申请通过 API 访问你账号的以下数据"),
    ("<b>Select all options</b>", "<b>全选</b>"),
    ("<b>User Info</b><span>Creator ID, profile, handle, region</span>", "<b>用户信息</b><span>达人 ID、资料、用户名、地区</span>"),
    ("<b>Content Posting</b><span>Upload and post shoppable videos, video metrics</span>", "<b>内容发布</b><span>上传和发布挂车视频、视频数据</span>"),
    ("<b>Showcase Products</b><span>Read and manage products in your showcase</span>", "<b>橱窗商品</b><span>查看和管理你橱窗里的商品</span>"),
    ("I agree that my data, as described above, will be…", "我同意上述数据将被……"),
    ('<a class="rej" href="#s10">Reject</a><a class="ok" href="#s4">Authorize</a>', '<a class="rej" href="#s10">拒绝</a><a class="ok" href="#s4">授权</a>'),

    # 4 connected
    ("<h2 class=\"title\">You're connected</h2>", "<h2 class=\"title\">连接成功</h2>"),
    ("Nothing has been posted yet. You don't need to do anything else.", "现在还没有发布任何内容，你不需要再做别的操作。"),
    ("US market · 4 permissions granted", "美国市场 · 已授权 4 项权限"),
    ("<h3>What happens next</h3>", "<h3>接下来会发生什么</h3>"),
    ("<b>Products added to your showcase</b><br>Only items in stock and approved by TikTok.", "<b>商品加入你的橱窗</b><br>只加有货、已通过 TikTok 审核的商品。"),
    ("<b>Videos reviewed by our studio</b><br>Each post is checked by a person and by TikTok's precheck.", "<b>工作室审核视频</b><br>每条视频都经过人工审核和 TikTok 预审。"),
    ("<b>First post goes live</b><br>You'll see it on your profile with a product link.", "<b>第一条视频发布</b><br>你会在主页看到它，带商品链接。"),
    ('<a class="btn" href="#s5" style="margin-top:8px">Open my workspace</a>', '<a class="btn" href="#s5" style="margin-top:8px">进入我的工作台</a>'),

    # 5 workspace
    ("<h2 class=\"hello\">Hi, Lena</h2>", "<h2 class=\"hello\">你好，Lena</h2>"),
    ("Week of Nov 24 · times in Pacific Time", "11 月 24 日这一周 · 时间为美西时间"),
    ("<b>14</b><span>Scheduled</span>", "<b>14</b><span>已排期</span>"),
    ("<b>9</b><span>Published</span>", "<b>9</b><span>已发布</span>"),
    ("<b>1</b><span>On hold</span>", "<b>1</b><span>暂停中</span>"),
    ("<b style=\"font-size:13px\">Today's posts</b><span class=\"small\">2 of 3</span>", "<b style=\"font-size:13px\">今日发布</b><span class=\"small\">2 / 3</span>"),
    ("TikTok's daily limit for your account is 3 shoppable videos.", "TikTok 对你账号的每日上限是 3 条挂车视频。"),
    ("<h3>Next up · 6:30 PM</h3>", "<h3>下一条 · 下午 6:30</h3>"),
    ("Precheck passed · Approved", "预审通过 · 已审批"),
    ("<h3>Needs your attention</h3>", "<h3>需要你留意</h3>"),
    ("<b style=\"font-size:13px\">1 post on hold</b><div class=\"small\">TikTok flagged a caption. We're fixing it.</div>", "<b style=\"font-size:13px\">1 条视频暂停中</b><div class=\"small\">TikTok 标记了一处文案，我们正在修改。</div>"),
    ('<span class="chip hold">Hold</span>', '<span class="chip hold">暂停</span>'),

    # 6 schedule
    ("<b>Schedule</b><span class=\"small\">Pacific Time</span>", "<b>排期</b><span class=\"small\">美西时间</span>"),
    ("Today · Mon, Nov 24", "今天 · 11 月 24 日 周一"),
    ("Tue, Nov 25", "11 月 25 日 周二"),
    ("<b>3-second makeup check</b>", "<b>3 秒检查妆容</b>"),
    ("<b>Laundry day, sorted</b>", "<b>洗衣日，分类搞定</b>"),
    ("<b>Movie night, upgraded</b>", "<b>电影之夜升级版</b>"),
    ("<b>Night shift glow-up</b>", "<b>夜班桌面焕新</b>"),
    ("<b>Travel-size glow</b>", "<b>旅行随身补光</b>"),
    ('<span class="time">10:00 AM</span>', '<span class="time">上午 10:00</span>'),
    ('<span class="time">1:30 PM</span>', '<span class="time">下午 1:30</span>'),
    ('<span class="time">6:30 PM</span>', '<span class="time">下午 6:30</span>'),
    ('<span class="time">11:00 AM</span>', '<span class="time">上午 11:00</span>'),
    ('<span class="time">5:00 PM</span>', '<span class="time">下午 5:00</span>'),
    ('<span class="chip ok">Published</span>', '<span class="chip ok">已发布</span>'),
    ('<span class="chip wait">Scheduled</span>', '<span class="chip wait">已排期</span>'),
    ('<span class="chip hold">On hold</span>', '<span class="chip hold">暂停中</span>'),
    ("On hold means TikTok's precheck found an issue. The post won't go live until it's fixed and approved again.",
     "暂停中表示 TikTok 预审发现问题；修改并重新审批前不会发布。"),

    # 7 detail
    ('<span class="ai">AI-generated</span>', '<span class="ai">AI 生成</span>'),
    ("<dt>Goes live</dt><dd>Today, 6:30 PM PT</dd>", "<dt>发布时间</dt><dd>今天 下午 6:30（美西）</dd>"),
    ("<dt>Product</dt>", "<dt>商品</dt>"),
    ("<dt>Commission</dt><dd>15% · open collaboration</dd>", "<dt>佣金</dt><dd>15% · 公开合作</dd>"),
    ("<dt>Product link title</dt><dd>Cozy Throw Blanket</dd>", "<dt>商品锚点标题</dt><dd>Cozy Throw Blanket</dd>"),
    ("<li>Product is in your showcase and in stock</li>", "<li>商品在你的橱窗里，且有货</li>"),
    ("<li>TikTok precheck passed</li>", "<li>TikTok 预审通过</li>"),
    ("<li>Approved by BLOOM GLOW studio · Nov 23</li>", "<li>BLOOM GLOW 工作室已审批 · 11 月 23 日</li>"),
    ("Ask to hold this post</a>", "申请暂停这条视频</a>"),
    ("You can delete any published post in TikTok, like your own videos.", "已发布的视频你可以在 TikTok 里直接删除，和你自己的视频一样。"),

    # 8 results
    ("<b>Results</b><span class=\"small\">Updated daily</span>", "<b>数据</b><span class=\"small\">每天更新</span>"),
    ('<span class="on">7 days</span><span>30 days</span><span>90 days</span>', '<span class="on">近 7 天</span><span>近 30 天</span><span>近 90 天</span>'),
    ("Sales from your posts", "你的视频带来的销售额"),
    ("63 orders · est. commission $327.60", "63 单 · 预估佣金 $327.60"),
    ("<span>Nov 17</span><span>Nov 23</span>", "<span>11/17</span><span>11/23</span>"),
    ("<h3>Top videos</h3>", "<h3>表现最好的视频</h3>"),
    ("Commission is paid by TikTok Shop to your account. Amounts here are estimates until TikTok settles them.",
     "佣金由 TikTok Shop 结算到你的账户；结算前这里显示的是预估金额。"),

    # 9 account
    ("<b>Account</b><span class=\"chip ok\">已连接</span>", "<b>账号</b><span class=\"chip ok\">已连接</span>"),
    ("US market · connected Nov 23", "美国市场 · 11 月 23 日连接"),
    ("<dt>Access</dt><dd>Renews automatically</dd>", "<dt>授权</dt><dd>自动续期</dd>"),
    ("<dt>Permissions</dt><dd>Profile, content posting, showcase, affiliate orders</dd>", "<dt>权限</dt><dd>账号资料、内容发布、橱窗、联盟订单</dd>"),
    ("<dt>Agreement</dt><dd>Up to 3 posts a day</dd>", "<dt>约定</dt><dd>每天最多 3 条</dd>"),
    ("<h3>Disconnect</h3>", "<h3>断开连接</h3>"),
    ("This deletes the access and data we store and stops all posting. Posts already on TikTok stay up.",
     "断开后，我们会删除保存的授权和数据，并停止所有发布；已发布在 TikTok 上的视频会保留。"),
    ('<a class="btn danger" href="#s1">Disconnect and delete</a>', '<a class="btn danger" href="#s1">断开并删除</a>'),
    ("To remove access on TikTok's side too, revoke <b>BLOOM GLOW Content Publishing</b> in your TikTok Shop authorization settings.",
     "如需同时撤销 TikTok 侧的授权，请在 TikTok Shop 授权设置中撤销 <b>BLOOM GLOW Content Publishing</b>。"),
    ("Questions: studioreadypost@gmail.com<br>We never ask for your TikTok password.", "有问题请联系：studioreadypost@gmail.com<br>我们绝不会索要你的 TikTok 密码。"),

    # 10 error
    ("<h2 class=\"title\">TikTok didn't connect your account</h2>", "<h2 class=\"title\">TikTok 没有完成授权</h2>"),
    ("TikTok showed \"Not available in your region.\" This is on our side: BLOOM GLOW is still waiting for TikTok's approval for US creators.",
     "TikTok 提示 \"Not available in your region\"（你所在地区不可用）。这是我们这边的原因：BLOOM GLOW 还在等 TikTok 对美区达人开放。"),
    ("<b style=\"font-size:13px\">What to do</b><p class=\"small\" style=\"margin:6px 0 0\">Nothing for now. We'll message you when it's ready, then tap the same link again.</p>",
     "<b style=\"font-size:13px\">怎么办</b><p class=\"small\" style=\"margin:6px 0 0\">暂时不用操作。开放后我们会通知你，再点一次同一个链接即可。</p>"),
    ("<h3>Other messages you might see</h3>", "<h3>你可能看到的其他提示</h3>"),
    ("<b>Use a US TikTok Shop creator</b><span>Your account's sales region isn't the US.</span>", "<b>请使用美区 TikTok Shop 达人账号</b><span>你账号的销售地区不是美国。</span>"),
    ("<b>Some permissions are missing</b><span>Connect again and tap \"Select all options.\"</span>", "<b>缺少部分权限</b><span>重新连接，并点\"全选\"。</span>"),
    ("<b>This link expired</b><span>Open the link again and start from the first step.</span>", "<b>链接已过期</b><span>重新打开链接，从第一步开始。</span>"),
    ('<a class="btn" href="#s2" style="margin-top:16px">Try again</a>', '<a class="btn" href="#s2" style="margin-top:16px">重试</a>'),
    ("Movie night, upgraded. This throw is unreal 🍿 #cozyhome #tiktokshop", "电影之夜升级版，这条毯子太舒服了 🍿 #cozyhome #tiktokshop"),
    ("Cloud Knit Throw · CTR 6.1%", "Cloud Knit Throw · 点击率 6.1%"),
    ("Glow Vanity Mirror · CTR 4.8%", "Glow Vanity Mirror · 点击率 4.8%"),
    ("Linen Hamper · CTR 3.9%", "Linen Hamper · 点击率 3.9%"),
]

out = src
missing = []
for a, b in T:
    if a not in out:
        missing.append(a[:70])
    out = out.replace(a, b)
(ROOT / "zh.html").write_text(out, encoding="utf-8")
print("replacements:", len(T), "missing:", len(missing))
for m in missing:
    print("  MISSING:", m)
