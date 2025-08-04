export function isNotEmpty(value, fieldname){
    if(!value.trim()){
        alert(`${fieldName} 항목을 입력하세요.`);
        return false;
    }
    return true;
}
//함수 외부로 가져가기