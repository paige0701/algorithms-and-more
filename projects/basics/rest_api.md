### REST API 

```
그냥 혼자 공부 하는 부분
```


Representational state transfer
Http URI를 통해 자원을 명시하고 HTTP method를 통해 해당 자원에 대한 CRUD operation
을 사용하는 것을 의미한다.

#### REST 구성
<hr/>
<ul>
    <li>자원 (resource) - URI</li>
    <li>행위 (verb) - http method</li>
    <li>표현 (representations) - data</li>
</ul>

#### REST 특징
<ul>
    <li>uniform interface - 통일성 있는 인터페이스를 얘기한다. 특정한 언어나 기술에 종속되지 
    않는 인터페이스.</li>
    <li>stateless - 서버는 클라이언트가 보내는 요청에 대한 정보를 저장하지 않는다.
    하나의 요청은 서버가 요청에 처리할 수 있는 모든 정보를 들고 있어야 한다. 전에 보냈던 정보를 저장하고
    있지 않는다</li>
    <li>cacheable - 웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를
    그대로 사용할 수 있다. last_modified, e-tag를 이용하면 캐싱 구현이 가능하다. </li>
    <li>self descriptiveness - REST API 만 보고 어떤 데이터를 요구하는지 알 수 있다. 
    [get] movies/1 -> 영화 1번 정보 주세요
    </li>
    <li>client server 구조 - 클라이언트랑 서버랑 분리된 구조. 서버는 클라이언트가 요청한 정보만 응답한다.</li>
    <li>layered system - 
    REST 서버는 다중 계층으로 구성될 수 있음 .. 보안, 로드밸런싱 등 계층을 추가해 구조상의 유연성을 둘 수 있다.
    proxy 도 사용 가능</li>
</ul>
