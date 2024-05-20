(self.webpackChunkdocusaurus=self.webpackChunkdocusaurus||[]).push([[951],{7379:(e,t,o)=>{"use strict";o.r(t),o.d(t,{Collapsible:()=>g.z,ErrorBoundaryError:()=>O.aG,ErrorBoundaryTryAgainButton:()=>O.Cw,ErrorCauseBoundary:()=>O.QW,HtmlClassNameProvider:()=>y.FG,NavbarSecondaryMenuFiller:()=>_.Zo,PageMetadata:()=>y.d,ReactContextError:()=>v.i6,SkipToContentFallbackId:()=>j.u,SkipToContentLink:()=>j.l,ThemeClassNames:()=>h.k,composeProviders:()=>v.Qc,createStorageSlot:()=>r.WA,duplicates:()=>F.l,filterDocCardListItems:()=>s.MN,isMultiColumnFooterLinks:()=>L.a,isRegexpStringMatch:()=>S.F,listStorageKeys:()=>r._f,listTagsByLetters:()=>T,prefersReducedMotion:()=>b.n,processAdmonitionProps:()=>R,translateTagsPageTitle:()=>C,uniq:()=>F.j,useCollapsible:()=>g.u,useColorMode:()=>w.I,useContextualSearchFilters:()=>a._q,useCurrentSidebarCategory:()=>s.jA,useDocsPreferredVersion:()=>I.J,useEvent:()=>v.zX,useIsomorphicLayoutEffect:()=>v.LI,usePluralForm:()=>m,usePrevious:()=>v.D9,usePrismTheme:()=>P.p,useSearchLinkCreator:()=>A,useSearchQueryString:()=>M,useStorageSlot:()=>r.Nk,useThemeConfig:()=>n.L,useWindowSize:()=>k.i});var n=o(86668),r=o(50012),a=o(43320),s=o(53438),i=o(67294),l=o(52263),u=o(25108);const c=["zero","one","two","few","many","other"];function d(e){return c.filter((t=>e.includes(t)))}const p={locale:"en",pluralForms:d(["one","other"]),select:e=>1===e?"one":"other"};function f(){const{i18n:{currentLocale:e}}=(0,l.default)();return(0,i.useMemo)((()=>{try{return function(e){const t=new Intl.PluralRules(e);return{locale:e,pluralForms:d(t.resolvedOptions().pluralCategories),select:e=>t.select(e)}}(e)}catch(t){return u.error(`Failed to use Intl.PluralRules for locale "${e}".\nDocusaurus will fallback to the default (English) implementation.\nError: ${t.message}\n`),p}}),[e])}function m(){const e=f();return{selectMessage:(t,o)=>function(e,t,o){const n=e.split("|");if(1===n.length)return n[0];n.length>o.pluralForms.length&&u.error(`For locale=${o.locale}, a maximum of ${o.pluralForms.length} plural forms are expected (${o.pluralForms.join(",")}), but the message contains ${n.length}: ${e}`);const r=o.select(t),a=o.pluralForms.indexOf(r);return n[Math.min(a,n.length-1)]}(o,t,e)}}var g=o(86043),h=o(35281),b=o(91442),v=o(902),y=o(10833),w=o(92949),_=o(13102),k=o(87524),E=o(95999);const C=()=>(0,E.I)({id:"theme.tags.tagsPageTitle",message:"Tags",description:"The title of the tag list page"});function T(e){const t={};return Object.values(e).forEach((e=>{const o=function(e){return e[0].toUpperCase()}(e.label);t[o]??=[],t[o].push(e)})),Object.entries(t).sort(((e,t)=>{let[o]=e,[n]=t;return o.localeCompare(n)})).map((e=>{let[t,o]=e;return{letter:t,tags:o.sort(((e,t)=>e.label.localeCompare(t.label)))}}))}var x=o(91980);function M(){return(0,x.Nc)("q")}function A(){const{siteConfig:{baseUrl:e,themeConfig:t}}=(0,l.default)(),{algolia:{searchPagePath:o}}=t;return(0,i.useCallback)((t=>`${e}${o}?q=${encodeURIComponent(t)}`),[e,o])}var L=o(42489),S=o(98022),F=o(67392),P=o(66412),I=o(60373);function R(e){const{mdxAdmonitionTitle:t,rest:o}=function(e){const t=i.Children.toArray(e),o=t.find((e=>i.isValidElement(e)&&"mdxAdmonitionTitle"===e.props?.mdxType)),n=i.createElement(i.Fragment,null,t.filter((e=>e!==o)));return{mdxAdmonitionTitle:o?.props.children,rest:n}}(e.children),n=e.title??t;return{...e,...n&&{title:n},children:o}}var j=o(55225),O=o(69690)},3158:function(e,t,o){"use strict";var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0});const r=n(o(67294)),a=n(o(93162));t.default=function(e){let{url:t,proxy:o}=e;return r.default.createElement("div",{style:{float:"right"},className:"dropdown dropdown--hoverable dropdown--right"},r.default.createElement("button",{className:"export-button button button--sm button--secondary"},"Export"),r.default.createElement("ul",{className:"export-dropdown dropdown__menu"},r.default.createElement("li",null,r.default.createElement("a",{onClick:e=>{e.preventDefault(),(e=>{let t;(e.endsWith("json")||e.endsWith("yaml")||e.endsWith("yml"))&&(t=e.substring(e.lastIndexOf("/")+1)),a.default.saveAs(e,t||"openapi.txt")})(`${t}`)},className:"dropdown__link",href:`${t}`},"OpenAPI Spec"))))}},39620:function(e,t,o){"use strict";var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0});const r=n(o(67294)),a=o(7379),s=n(o(44996)),i=n(o(50941));t.default=function(e){const{colorMode:t}=(0,a.useColorMode)(),{logo:o,darkLogo:n}=e,l=()=>"dark"===t?n?.altText??o?.altText:o?.altText,u=(0,s.default)(o?.url),c=(0,s.default)(n?.url);return o&&n?r.default.createElement(i.default,{alt:l(),sources:{light:u,dark:c},className:"openapi__logo"}):o||n?r.default.createElement(i.default,{alt:l(),sources:{light:u??c,dark:u??c},className:"openapi__logo"}):void 0}},94303:(e,t,o)=>{"use strict";o.r(t),o.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>d,frontMatter:()=>a,metadata:()=>i,toc:()=>u});var n=o(87462),r=(o(67294),o(3905));o(39620),o(9472),o(85162),o(3158);const a={id:"fastapi",title:"FastAPI",description:"",sidebar_label:"Introduction",sidebar_position:0,hide_title:!0,custom_edit_url:null},s=void 0,i={unversionedId:"youtube-rss-api/fastapi",id:"youtube-rss-api/fastapi",title:"FastAPI",description:"",source:"@site/docs/youtube-rss-api/fastapi.info.mdx",sourceDirName:"youtube-rss-api",slug:"/youtube-rss-api/fastapi",permalink:"/docs/youtube-rss-api/fastapi",draft:!1,editUrl:null,tags:[],version:"current",sidebarPosition:0,frontMatter:{id:"fastapi",title:"FastAPI",description:"",sidebar_label:"Introduction",sidebar_position:0,hide_title:!0,custom_edit_url:null},sidebar:"openApiSidebar",previous:{title:"Youtube rss API",permalink:"/docs/category/youtube-rss-api"},next:{title:"Get Feed",permalink:"/docs/youtube-rss-api/get-feed-api-feed-get"}},l={},u=[],c={toc:u};function d(e){let{components:t,...o}=e;return(0,r.kt)("wrapper",(0,n.Z)({},c,o,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("span",{className:"theme-doc-version-badge badge badge--secondary"},"Version: 0.1.0"),(0,r.kt)("h1",{className:"openapi__heading"},"FastAPI"))}d.isMDXComponent=!0},93162:function(e,t,o){var n,r,a,s=o(25108);r=[],void 0===(a="function"==typeof(n=function(){"use strict";function t(e,t){return void 0===t?t={autoBom:!1}:"object"!=typeof t&&(s.warn("Deprecated: Expected third argument to be a object"),t={autoBom:!t}),t.autoBom&&/^\s*(?:text\/\S*|application\/xml|\S*\/\S*\+xml)\s*;.*charset\s*=\s*utf-8/i.test(e.type)?new Blob(["\ufeff",e],{type:e.type}):e}function n(e,t,o){var n=new XMLHttpRequest;n.open("GET",e),n.responseType="blob",n.onload=function(){u(n.response,t,o)},n.onerror=function(){s.error("could not download file")},n.send()}function r(e){var t=new XMLHttpRequest;t.open("HEAD",e,!1);try{t.send()}catch(e){}return 200<=t.status&&299>=t.status}function a(e){try{e.dispatchEvent(new MouseEvent("click"))}catch(n){var t=document.createEvent("MouseEvents");t.initMouseEvent("click",!0,!0,window,0,0,0,80,20,!1,!1,!1,!1,0,null),e.dispatchEvent(t)}}var i="object"==typeof window&&window.window===window?window:"object"==typeof self&&self.self===self?self:"object"==typeof o.g&&o.g.global===o.g?o.g:void 0,l=i.navigator&&/Macintosh/.test(navigator.userAgent)&&/AppleWebKit/.test(navigator.userAgent)&&!/Safari/.test(navigator.userAgent),u=i.saveAs||("object"!=typeof window||window!==i?function(){}:"download"in HTMLAnchorElement.prototype&&!l?function(e,t,o){var s=i.URL||i.webkitURL,l=document.createElement("a");t=t||e.name||"download",l.download=t,l.rel="noopener","string"==typeof e?(l.href=e,l.origin===location.origin?a(l):r(l.href)?n(e,t,o):a(l,l.target="_blank")):(l.href=s.createObjectURL(e),setTimeout((function(){s.revokeObjectURL(l.href)}),4e4),setTimeout((function(){a(l)}),0))}:"msSaveOrOpenBlob"in navigator?function(e,o,s){if(o=o||e.name||"download","string"!=typeof e)navigator.msSaveOrOpenBlob(t(e,s),o);else if(r(e))n(e,o,s);else{var i=document.createElement("a");i.href=e,i.target="_blank",setTimeout((function(){a(i)}))}}:function(e,t,o,r){if((r=r||open("","_blank"))&&(r.document.title=r.document.body.innerText="downloading..."),"string"==typeof e)return n(e,t,o);var a="application/octet-stream"===e.type,s=/constructor/i.test(i.HTMLElement)||i.safari,u=/CriOS\/[\d]+/.test(navigator.userAgent);if((u||a&&s||l)&&"undefined"!=typeof FileReader){var c=new FileReader;c.onloadend=function(){var e=c.result;e=u?e:e.replace(/^data:[^;]*;/,"data:attachment/file;"),r?r.location.href=e:location=e,r=null},c.readAsDataURL(e)}else{var d=i.URL||i.webkitURL,p=d.createObjectURL(e);r?r.location=p:location.href=p,r=null,setTimeout((function(){d.revokeObjectURL(p)}),4e4)}});i.saveAs=u.saveAs=u,e.exports=u})?n.apply(t,r):n)||(e.exports=a)}}]);